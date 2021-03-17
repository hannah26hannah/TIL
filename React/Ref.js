import React, { Component } from 'react';

class Ref extends Component {
  input = React.createRef();

  handleFocus = () => {
    this.input.current.focus();
  };

  render() {
    return (
      <div>
        <input ref={this.input} />
        <button onClick={this.handleFocus}>Click to Focus</button>
      </div>
    );
  }
}

export default Ref;
