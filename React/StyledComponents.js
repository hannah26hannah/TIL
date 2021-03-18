import React from 'react';
import styled, { css } from 'styled-components';

const sizes = {
  desktop: 1024,
  tablet: 768,
};
const media = Object.keys(sizes).reduce((acc, label) => {
  acc[label] = (...args) => css`
    @media (max-width: ${sizes[label] / 16}em) {
      ${css(...args)};
    }
  `;
  return acc;
}, {});

const Box = styled.div`
  background: ${(props) => props.color || 'blue'};
  padding: 1rem;
  display: flex;
  /* 가로 크기 1024px 가운데 정렬 가로 크기는 작아지면서 크기가 줄어들며 768px 미만이 될 경우 Full Screen */
  width: 1024px;
  margin: 0 auto;
  ${media.desktop`width: 768px;`};
  ${media.tablet`width: 100%;`};

  /* @media (max-width: 1024px) {
    width: 768px;
  }
  @media (max-width: 768px) {
    width: 100%;
  } */
`;

const Button = styled.button`
  background: white;
  color: black;
  border-radius: 4px;
  padding: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  font-size: 1rem;
  font-weight: 600;

  /* & 문자 사용 Like Sass */
  &:hover {
    background: rgba(255, 255, 255, 0.9);
  }

  /* 다음 코드는 inverted 값이 true일 때 특정 스타일을 부여한다. */
  ${(props) =>
    props.inverted &&
    css`
      background: none;
      border: 2px solid white;
      color: white;
      &:hover {
        background: white;
        color: black;
      }
    `};
  & + button {
    margin-left: 1rem;
  }
`;

const StyledComponents = () => (
  <Box color="black">
    <Button>안녕!</Button>
    <Button inverted={true}>테두리만</Button>
  </Box>
);

export default StyledComponents;
