import React from 'react';

const Card = ({ title , contentCard}) => {
  return (
    <div className="card">
      <div className="card-body">
        <h5 className="card-title">{title}</h5>
        <p className="card-text">{contentCard}</p>
      </div>
    </div>
  );
};

export default Card;
