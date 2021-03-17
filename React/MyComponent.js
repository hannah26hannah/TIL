import React, { Component } from 'react';
import PropTypes from 'prop-types';

class MyComponent extends Component {
  static defaultProps = {
    name: '기본 이름',
  };
  static propTypes = {
    name: PropTypes.string,
    favoriteNumber: PropTypes.number.isRequired,
  };
  render() {
    const { name, children, favoriteNumber } = this.props;
    return (
      <div>
        안녕! 내 이름은 {name}. <br />
        Children 값은 {children} 입니다. 가장 좋아하는 숫자는 {favoriteNumber}
        입니다.
      </div>
    );
  }
}

export default MyComponent;
