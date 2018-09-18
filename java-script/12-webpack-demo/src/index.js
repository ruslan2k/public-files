import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import PropTypes from 'prop-types'
import { createStore, applyMiddleware } from 'redux'
import { Provider, connect } from 'react-redux'
import axios from 'axios'
import './styles/app.css'
import { DEF_DOMAIN } from './config'
import { fetchArchives, resize } from './actions'
import { logger, apiMiddleware, timelineMiddleware } from './middleware'
import reducer from './reducer'
import Interval from './components/interval'
import TimeRange from './components/TimeRange'

const getActiveIntervals = (intervals, xMinute) => {
  return intervals.filter((interval) => {
    const stopOffset = interval.stop.getHours() * 60 + interval.stop.getMinutes()
    return (xMinute < stopOffset)
  })
}

const getActualOffset = (interval, xMinute) => {
  const startMinute = interval.start.getHours() * 60 + interval.start.getMinutes()
  const stopMinute = interval.stop.getHours() * 60 + interval.stop.getMinutes()
  if (startMinute < xMinute && stopMinute > xMinute) {
    const date = new Date(interval.start.toDateString())
    return new Date(date.getTime() + (xMinute * 60 * 1000))
  }
  return interval.start
}

class Timeline extends Component {
  constructor(props) {
    super(props)
    this.state = {actualMinute: 0}
    // This binding is necessary to make `this` work in the callback
    this.timeLineClick = this.timeLineClick.bind(this)
  }

  resize() {
    const width = document.getElementById("t-r").clientWidth
    this.setState({ width })
  }

  timeLineClick(xCoord) {
    const intervals = this.props.intervals
    const activeIntervals = getActiveIntervals(intervals, xCoord)
    const currentInterval = (activeIntervals.length) ? activeIntervals[0] : intervals.slice(-1)[0]
    const actualOffset = getActualOffset(currentInterval, xCoord)
    const actualMinute = actualOffset.getHours() * 60 + actualOffset.getMinutes();
    this.setState({actualMinute: actualMinute})
  }

  componentDidMount() {
    this.props.fetchArchives()
    this.resize()
    window.addEventListener('resize', this.resize.bind(this))
  }

  componentWillUnmount() {
    window.removeEventListener('resize', this.resize.bind(this))
  }

  render() {
    const width = (this.state && this.state.width) ? this.state.width : null
    const intervals = this.props.intervals.map((interval, index) =>
      <Interval key={index} parentWidth={width} {...interval} />
    )
    const uiStyle = {
      position: "absolute",
      left: 0,
      right: 0,
      width: '100%'
    }
    return (
      <div>
        <p>Timeline</p>
        <div>
          {/*
          <ul style={uiStyle}>
            <li>0:00</li><li>1:00</li><li>2:00</li><li>3:00</li><li>4:00</li>
            <li>5:00</li><li>6:00</li><li>7:00</li><li>8:00</li><li>9:00</li>
            <li>10:00</li><li>11:00</li><li>12:00</li><li>13:00</li><li>14:00</li>
            <li>15:00</li><li>16:00</li><li>17:00</li><li>18:00</li><li>19:00</li>
            <li>20:00</li><li>21:00</li><li>22:00</li><li>23:00</li><li>24:00</li>
          </ul>
          */}
          <TimeRange onClick={this.timeLineClick} actualMinute={this.state.actualMinute} />
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

ReactDOM.render(
  <div>
    <Provider store={store}>
      <VisibleTimeline />
    </Provider>
  </div>,
  document.getElementById('timeline')
)
