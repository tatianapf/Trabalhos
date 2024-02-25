CREATE DATABASE TP_Cabeleireiro;
GO
USE TP_Cabeleireiro;
GO 
CREATE TABLE cliente
    (
      IdCliente INT NOT NULL IDENTITY , /*SQL Server*/
      NIF BIGINT ,	 
      Nome VARCHAR(250),
      Morada VARCHAR(250),
      Email VARCHAR(250) ,
      Telemovel BIGINT ,
	  PRIMARY KEY (IdCliente)
    );


CREATE TABLE TipoPagamento
     (
      IdTipoPagamento INT NOT NULL,
	  PRIMARY KEY (IdTipoPagamento),
	  NomePagamento VARCHAR(250) NOT NULL

    );

CREATE TABLE fatura
    (
	  IdFatura INT NOT NULL IDENTITY, /*SQL Server*/
      IdCliente INT,
      IdTipoPagamento INT,
	  PRIMARY KEY (IdFatura),
	  Foreign key (IdCliente) References cliente(IdCliente),
	  Foreign key (IdTipoPagamento) References TipoPagamento(IdTipoPagamento),
	  DataEmissao Date ,
	  PrecoI FLOAT ,
	  NomePagamento VARCHAR(250) NOT NULL,
	  Constraint chk_Nome CHECK (NomePagamento IN('Numerario', 'Transferencia', 'Paypal', 'Cheque', 'MBway')),
	  
  
  
    );

CREATE TABLE servico
    (
      IdServico INT NOT NULL, /*SQL Server*/
      PRIMARY KEY (IdServico),
	  NomeServico VARCHAR(250) NOT NULL,
	  Preco FLOAT,
	  TaxaIva FLOAT
	 
	  
    );

CREATE TABLE LinhaFatura
    (
	IdFatura INT NOT NULL,
	IdServico INT NOT NULL,
	PRIMARY KEY (IdFatura, IdServico),
	Foreign key (IdFatura) References fatura(IdFatura),
	Foreign key (IdServico) References servico(IdServico),
	PrecoI FLOAT ,
	DataEmissao Date,
	Quantidade INT

	);

