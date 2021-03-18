import React from 'react';
import useInputs from './useInputs';

const ImprovedInfo = () => {
  const [state, onChange] = useInputs({
    name: '',
    nickname: '',
  });
  const { name, nickname } = state;

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
export default ImprovedInfo;
