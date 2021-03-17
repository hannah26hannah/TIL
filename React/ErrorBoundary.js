import React, { Component } from 'react';

class ErrorBoundary extends Component {
  state = {
    error: false,
  };
  componentDidCatch(error, info) {
    this.setState({
      error: true,
    });
    console.log({ error, info });
  }

  render() {
    if (this.state.error) return <h1>에러가 발생했습니다.</h1>;
    return this.props.children;
  }
}

export default ErrorBoundary;
