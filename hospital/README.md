# Modelado

## Sprint 1, Modelado
- Paciente
- Cita
- Doctor
- Sala
- Especialidad
- Registro clinico

Ojetvos y sus atributos

doctor_hospital
-----------------------
- id int (PK)
- id_especialidad int (FK)
- foto binary
- nombre varchar
- apellido varchar
- celular varchar(9)
- n_colegiatura char

paciente_hospital
---------------
- id int (PK)
- dni varchar
- apellido
- celular varchar (9)
- edad char

cita_hospital
--------------
- cita_ id int (PK)
- cod_cita char 
- id_doctor int (FK)
- id_sala int (FK)
- id_paciente int (FK)
- fecha datetime
- especialidad varchar

registroclinico_hospital
-----------------------
- id int (PK)
- cod_registro char
- id_paciente int (FK)
- diagnostico varchar
- receta varchar
- examen varchar

especialidad_hospital
---------------------
- id int (PK)
- cod_especialidad varchar
- nombre_especialidad varchar

sala_hospital
--------------
- id int
- n_sala char
- ubicacion varchar

Esquema relacional
doctor_hospital (muchos) a (muchos) especialidad_hospital
