import React from 'react';
import Navbar from './Navbar';

const About = () => {
  return (
    <>
      <Navbar></Navbar>
      <div className="container mt-5">
        <div className="card">
          <div className="card-body">
            <h5 className="card-title">Sobre o projeto</h5>
            <p className="card-text">Monitoramento de incêndio</p>
          </div>
        </div>
      </div>
    </>
  );
};

export default About;
