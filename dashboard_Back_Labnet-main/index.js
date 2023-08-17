import express from "express";

import { Sequelize, DataTypes } from "sequelize";

const app = express()

// passar as credenciais do banco, onde ele tá, o tipo, senha ...
const sequelize = new Sequelize('lens','buda','password',{

  host: 'localhost',

  dialect: 'mariadb'

});

//testando a conexão
try {

  await sequelize.authenticate();

  console.log('A conexão foi estabelecida com sucesso');

} catch(error){

  console.error('Sem conexão com o banco de dados', error);

}

// definindo os modelos, como o código vai interpretar as tabelas do banco de dados
 const sensores = sequelize.define('sensores', {

 id: {

  type: DataTypes.INTEGER,

  allowNull: false,

  autoIncrement: true,

  primaryKey: true

 },

 data:{

  type: DataTypes.DATE,

  allowNull: false

 },

 co2:{

  type: DataTypes.INTEGER,

  allowNull: false

 },

 temperatura:{ 

  type: DataTypes.INTEGER,

  allowNull: false

 },

 luz: {

  type: DataTypes.INTEGER,

  allowNull: false

}

 }, {

  timestamps: false
  
});

//sincronização

(async () => {

await sequelize.sync();

 })();

 //rotas
 app.get('/sensores',async (req, res) => {

  const dadosSensores = await sensores.findAll();

  res.send(dadosSensores)

  //res.send('Hello World!')

 })


app.get('/',(req, res) => {

  res.send('Hello World!')

})

app.listen(3000, ()=> console.log("Servidor rodando"))