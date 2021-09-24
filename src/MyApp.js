import React, {useState} from 'react';
import Table from './Table';

function MyApp() {
  const [characters, setCharacters] = useState([
      {
        name: 'Charlie',
        job: 'Janitor',
         // the rest of the data
      },
      {
        name: 'jon',
        job: 'best friend',
      },
      {
        name: 'jax',
        job: 'joker',
      },
    ]);

function removeOneCharacter (index) {
  const updated = characters.filter((character, i) => {
      return i !== index
    });
    setCharacters(updated);
  }
  return (
    <div className="container">
      <Table characterData={characters} removeCharacter={removeOneCharacter} />
    </div>
  )
}


export default MyApp;