import React, { Component } from 'react';

class LifeCycleSample extends Component {
  state = {
    number: 0,
    color: null,
  };

  myRef = null; // ref를 설정할 부분

  constructor(props) {
    super(props);
    console.log('constructor');
  }

  static getDerivedStateFromProps(nextProps, prevState) {
    console.log('getDerivedStateFromProps');
    // 부모에게 받은 color 값을 state에 동기화하고 있다.
    if (nextProps.color !== prevState.color) {
      return { color: nextProps.color };
    }
    return null;
  }
  componentDidMount() {
    console.log('componentdidmount');
  }

  shouldComponentUpdate(nextProps, prevState) {
    console.log('shouldComponentUpdate', nextProps, prevState);
    return nextProps.number % 10 !== 4; // 숫자의 마지막 자리가 4일 경우 렌더링하지 않는다.
  }

  componentWillUnmount() {
    console.log('componentWillUnmount');
  }

  handleclick = () => {
    this.setState({
      number: this.state.number + 1,
    });
  };

  getSnapshotBeforeUpdate(prevProps, prevState) {
    console.log('getSnapshotBeforeUpdate');
    // DOM 변화가 일어나기 전 색상 속성을 snapshot 값으로 반환해 이를 componentDidUpdate에서 조회하도록 한다.
    if (prevProps.color !== this.props.color) {
      return this.myRef.style.color;
    }
    return null;
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    console.log('componentdidupdate', prevProps, prevState);
    if (snapshot) {
      console.log('업데이트 되기 직전 색상', snapshot);
    }
  }

  render() {
    console.log('render');
    const style = {
      color: this.props.color,
    };

    return (
      <div>
        {this.props.missing.value}
        <h1 style={style} ref={(ref) => (this.myRef = ref)}>
          {this.state.number}
        </h1>
        <p>Color: {this.state.color}</p>
        <button onClick={this.handleclick}>더하기</button>
      </div>
    );
  }
}

export default LifeCycleSample;
