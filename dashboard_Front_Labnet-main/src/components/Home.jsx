import React from 'react';
import Card from './Card';
import Navbar from './Navbar';
import {
  Chart,
  ArcElement,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  PointElement,
  LineElement,
  Filler,
} from 'chart.js'
import { Bar } from "react-chartjs-2";
import { faker } from "@faker-js/faker"

Chart.register(
  ArcElement,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  PointElement,
  LineElement,
  Filler,
);

const Home = () => {

  const cards = [
    {
      titulo: "Temperatura",
      corpo: "22cº"
    },
    {
      titulo: "Co2",
      corpo: "400 ppm"
    },
    {
      titulo: "Luminosidade",
      corpo: "1 Lúmen"
    },
    {
      titulo: "Risco",
      corpo: "Sem Risco"
    },
  ]
// const graf1 = fetch("http://localhost:5000/graf1")
  //   .then((data) => data)
  //   .catch((error) => console.error(error))
  const graf1 = {
    labels: ['Horários'],
    datasets: [
      {
        label: 'Temperatura',
        data: [12, 19, 3],
        backgroundColor: ['#3F51B5']
      }
    ]
  };
  // const graf2 = fetch("http://localhost:5000/graf2")
  //   .then((data) => data)
  //   .catch((error) => console.error(error))
  const graf2 = {
    labels: ['Horários'],
    datasets: [
      {
        label: 'Luminosidade',
        data: [12, 19, 3],
        backgroundColor: ['#3F51B5']
      }
    ]
  };
  // const graf3 = fetch("http://localhost:5000/graf3")
  //   .then((data) => data)
  //   .catch((error) => console.error(error))
  const graf3 = {
    labels: ['Horários'],
    datasets: [
      {
        label: 'CO2',
        data: [12, 19, 3],
        backgroundColor: ['#3F51B5']
      }
    ]
  };

  const options = {
    responsive: true
  };

  const labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'];

  const data = {
    labels,
    datasets: [
      {
        label: 'Temperatura',
        data: [18, 19, 20, 18, 17, 20, 21, 22, 22, 23, 23, 24, 28, 28, 27, 26, 27,],
        backgroundColor: 'rgba(63, 81, 181, 1)',
      },
    ],
  };

  return (
    <>
      <Navbar></Navbar>
      <div className="container mt-5">
        <h1 className="boas-vindas">Bem-vindo à página inicial!</h1>
        <div className="row mt-5">
          {
            cards.map((item, idx) => {
              return (
                <div className="col">
                  <Card title={item.titulo} contentCard={item.corpo} />
                </div>)
            })
          }
        </div>
        <div className="row mt-5">
          <div className="col mt-5" style={{ height: "150px", width: "150px" }}>
            <Bar data={data} options={options} />
          </div>
          <div className="col mt-5" style={{ height: "150px", width: "150px" }}>
            <Bar data={graf2} options={options} />
          </div>
          <div className="col mt-5" style={{ height: "150px", width: "150px" }}>
            <Bar data={graf3} options={options} />
          </div>
        </div>
      </div>
    </>
  );
};

export default Home;
