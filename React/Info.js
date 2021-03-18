import React, { useReducer } from 'react';
import useInputs from './useInputs';

function reducer(state, action) {
  return {
    ...state,
    [action.name]: action.value,
  };
}
const Info = () => {
  // const [state, dispatch] = useReducer(reducer, { name: '', nickname: '' });
  const [state, onChange] = useInputs({
    name: '',
    nickname: '',
  });
  const { name, nickname } = state;
  // const onChange = (e) => {
  //   dispatch(e.target);
  // };
  return (
    <main>
      <section>
        <input
          name="name"
          value={name}
          onChange={onChange}
          placeholder="write your name"
        />
        <input
          name="nickname"
          value={nickname}
          onChange={onChange}
          placeholder="write your name"
        />
      </section>
      <section>
        이름 : {name}, 닉네임 : {nickname}
      </section>
    </main>
  );
};
export default Info;
