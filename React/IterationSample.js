import React, { useState } from 'react';

const IterationSample = () => {
  const [names, setNames] = useState([
    { id: 1, text: '✅' },
    { id: 2, text: '📚' },
    { id: 3, text: '❕' },
    { id: 4, text: '👉' },
    { id: 5, text: '🙌' },
  ]);

  const [inputText, setInputText] = useState('');

  const [nextId, setNextId] = useState(6); // 새로운 항목을 추가할 때 사용할 id

  const onChange = (e) => setInputText(e.target.value);

  const onRemove = (id) => {
    const nextNames = names.filter((name) => name.id !== id);
    setNames(nextNames);
  };
  const namesList = names.map((name) => (
    <li key={name.id} onDoubleClick={() => onRemove(name.id)}>
      {name.text}
    </li>
  ));

  const onClick = (e) => {
    const nextNames = names.concat({ id: nextId, text: inputText });
    setNextId(nextId + 1);
    setNames(nextNames);
    setInputText('');
  };
  return (
    <>
      <input
        type="text"
        value={inputText}
        onChange={onChange}
        placeholder="Add Unique Emoji"
      />
      <button onClick={onClick}>Add</button>
      <ul>{namesList}</ul>
    </>
  );
};
export default IterationSample;
