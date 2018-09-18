import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import { MINUTES_IN_A_DAY } from '../constants'

class TimeRange extends Component {
  constructor(props) {
    super(props);
    this.state = { width: 1 };
    this.handleClick = this.handleClick.bind(this);
  }

  componentDidMount() {
    const rect = ReactDOM.findDOMNode(this);
    const width = rect.getBoundingClientRect().width;
    this.setState({ width })
  }

  handleClick(event) {
    const rect = ReactDOM.findDOMNode(this);
    const width = rect.getBoundingClientRect().width;
    const x = event.pageX - rect.getBoundingClientRect().x
    const minute = (MINUTES_IN_A_DAY * x / width).toFixed()
    this.props.onClick(minute)  // Escalate click event
  }

  render() {
    const width = this.state.width;
    const actualMinute = this.props.actualMinute || 1;
    const xPix = (actualMinute * width / MINUTES_IN_A_DAY).toFixed();
    const style = {
      left: xPix + 'px',
    }
    return (
      <div id="t-r" className="time-range" onClick={this.handleClick}>
        <span style={style} className="time-current"></span>
      </div>
    )
  }
}

export default TimeRange
