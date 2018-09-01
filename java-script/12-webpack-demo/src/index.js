import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'
import $ from 'jquery'
import './styles/app.css'

class Timeline extends Component {
  render() {
    return (
      <div>
        <h1>Timeline</h1>
        <div>
          <ul>
            <li>0:00</li>
            <li>1:00</li>
            <li>...</li>
            <li>24:00</li>
          </ul>
          <div id="t-r" class="time-range">
            <span class="time-current"></span>
          </div>
          <div class="timeline">
            <span id="s1" class="time-selection">s1</span>
            <span id="s2" class="time-selection">s2</span>
          </div>
        </div>
      </div>
    )
  }
}

var App = (function () {
  var MIN_IN_DAY = 1440
  var blockWidth = $('.time-range').width()
  var minutesInPixel = MIN_IN_DAY / blockWidth

  const createIntervals = (archives) => {
    var intervals = []
    var l = archives.length
    for (var i = 0, j = 0; i < l; i ++) {
      var archive = archives[i]
      var interval = {archives: []}
      console.log(archive)
      if (! intervals[j]) {
        interval.start = archive.start_dt
        interval.stop = archive.stop_dt
        interval.archives.push(archive)
        intervals[j] = interval
        continue
      }
      var stopTime = new Date(intervals[j].stop)
      var startTime = new Date(archive.start_dt)
      if (Math.abs(startTime - stopTime) > 60000) {
        j += 1
        interval.start = archive.start_dt
        interval.stop = archive.stop_dt
        interval.archives.push(archive)
        intervals[j] = interval
        continue
      }
      intervals[j].stop = archive.stop_dt
      intervals[j].archives.push(archive)
    }
    return intervals
  }

  const init = () => {
    $(window).on('resize', function () {
      blockWidth = $('.time-range').width()
      minutesInPixel = MIN_IN_DAY / blockWidth
      console.log('minInPixel', minutesInPixel)
      axios.get(DOMAIN + '/json')
        .then(resp => {
          console.log(resp.data)
          console.log(createIntervals(resp.data.archives))
        })
        .catch(err => console.log(err))
    })
    $('.time-range').on('click', function (event) {
      // console.log(event.pageX, event.pageY);
      $('.time-current').css('left', event.pageX + 'px')
      var posX = $(this).offset().left
      var posY = $(this).offset().top
      var x = event.pageX - posX
      var currentMinute = x * minutesInPixel
      var hour = currentMinute / 60
      console.log('x', x)
      console.log('currentMinute', currentMinute)
      console.log('hour', hour)
    })
  }

  return {
    init
  }
}())

$(function () {
  // App.init()
})

ReactDOM.render(
  <Timeline />,
  document.getElementById('timeline')
)
