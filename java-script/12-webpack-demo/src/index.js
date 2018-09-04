import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'
import { createStore, applyMiddleware } from 'redux'
import { Provider, connect } from 'react-redux'
import axios from 'axios'
import $ from 'jquery'
import './styles/app.css'
import { DEF_DOMAIN } from './config'
import { fetchArchives, resize } from './actions'
import { logger, apiMiddleware, timelineMiddleware } from './middleware'
import reducer from './reducer'

const Interval = (props) => {
  return <span className="time-selection">{props.parentWidth}</span>
}

class Timeline extends Component {
  resize() {
    const width = document.getElementById("t-r").clientWidth
    this.setState({ width })
  }

  componentDidMount() {
    this.props.fetchArchives()
    window.addEventListener('resize', this.resize.bind(this))
    this.resize()
  }

  componentWillUnmount() {
    window.removeEventListener('resize', this.resize.bind(this))
  }

  render() {
    console.log('render')
    const width = (this.state && this.state.width) ? this.state.width : null
    const intervals = this.props.intervals.map((interval, index) =>
      <Interval key={index} parentWidth={width} />
    )
    return (
      <div>
        <p>Timeline</p>
        <div>
          <ul>
            <li>0:00</li>
            <li>1:00</li>
            <li>...</li>
            <li>24:00</li>
          </ul>
          <div id="t-r" className="time-range">
            <span className="time-current"></span>
          </div>
          <div className="timeline">
            {intervals}
          </div>
        </div>
      </div>
    )
  }
}

Timeline.propTypes = {
  fetchArchives: PropTypes.func.isRequired
}

const mapStateToProps = state => {
  return {
    intervals: state.intervals
  }
}

const mapDispatchToProps = dispatch => {
  return {
    fetchArchives: () => dispatch(fetchArchives())
  }
}

const VisibleTimeline = connect(
  mapStateToProps,
  mapDispatchToProps
)(Timeline)

var store = createStore(
  reducer,
  applyMiddleware(
    logger,
    apiMiddleware,
    timelineMiddleware
))

var App = (function () {

  const init = () => {
    $(window).on('resize', function () {
      blockWidth = $('.time-range').width()
      minutesInPixel = MIN_IN_DAY / blockWidth
      console.log('minInPixel', minutesInPixel)
      axios.get(DEF_DOMAIN + '/json')
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
  <div>
    <Provider store={store}>
      <VisibleTimeline />
    </Provider>
  </div>,
  document.getElementById('timeline')
)
