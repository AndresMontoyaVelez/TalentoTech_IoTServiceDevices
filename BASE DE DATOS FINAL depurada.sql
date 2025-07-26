CREATE DATABASE `projectciber`;
USE `projectciber`;
CREATE TABLE IF NOT EXISTS `employees` (
  `IdEmploy` int(10) UNSIGNED NOT NULL,
  `NameEmploy` varchar(100) NOT NULL,
  `ApellidoEmploy` varchar(100) NOT NULL,
  `EmailEmploy` varchar(100) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `IdRoles` int(10) UNSIGNED NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

INSERT INTO `employees` (`IdEmploy`, `NameEmploy`, `ApellidoEmploy`, `EmailEmploy`, `Password`, `IdRoles`) VALUES
(7, 'usuario1', 'usuario1', 'usuario1@gmail.com', '$2b$12$WfHlvWgyunjzRSpQRZqrme7X6/ymYbSwGCVr2qSy6.LnlhVI68KLa', 3),
(8, 'Julian piñares', 'Julian piñares', 'Jpinares@tigrillos.com', '$2b$12$oERIjnVUPZqInfMsNoR8R.a/K/xN2PcRzxwNVBIrqq2N3gnTVHObW', 1),
(9, 'Juan Rios', 'Juan Rios', 'jrios@tigrillos.com', '$2b$12$7ih7mezZDrMZ6EqKZJrsOe5FcbbYppbcjtfhl8h/GUBrhZvBzk/qC', 2),
(10, 'david suarez', 'david suarez', 'dsuarez@tigrillos.com', '$2b$12$jwaH4xg/XxYDzlhE.iOAgupl9bh49Z1nxMW95yP1lYTuUTcv5dL7i', 2),
(11, 'miguel gomez', 'miguel gomez', 'mgomez@tigrillos.com', '$2b$12$euz6nCO8oHA.xfIajhZMRetxk.yTh4CS/vaX7pZMh7ufat7W9qfTe', 1),
(12, 'andres montoya velez', 'andres montoya velez', 'amontoya@tigrillos.com', '$2b$12$.aSxwpSOW8OO6FDYenNThuW9km5v3yemDfG.uKgn9m0rjoHsWlzfO', 2),
(14, 'javier', 'javier', 'javier@gmail.com', '$2b$12$8rptOgMMc.1lV4QpQG4X0.LWqHOtF9gV0.4hD6diREzq5YgtjmIjC', 3),
(105, 'oooo', 'oooo', 'oooo@o.com', '$2b$12$HYXwBcm7NYWUSi.pQIxKSuEgdMxYnyDLl73B2fMCHCi/Jo9ck3EFq', 3),
(106, 'josefina', 'josefina', 'josefa@josefa.com', '$2b$12$aRWiiu/yhCkltlNKt.GE5.Zpwu.tlJYw4cdkXcb6aspcX391UMBja', 3),
(107, 'Dorian', 'Dorian', 'dorian@siu.com', '$2b$12$Oc.xs1kaKHS.Jkg5IWLiw.JCRv63M6rDJa3W/buHbet8ne3xQCu96', 3),
(108, 'joseph', 'joseph', 'joseph@hotmail.com', '$2b$12$Y0RA9ihm6mjUR77ZAPI4VueN3.fC2Yialy8HOuVFWhQTswUufBq4u', 3);

CREATE TABLE IF NOT EXISTS `roles` (
  `IdRoles` int(10) UNSIGNED NOT NULL,
  `RolName` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

INSERT INTO `roles` (`IdRoles`, `RolName`) VALUES
(1, 'Administrador'),
(2, 'Empleados'),
(3, 'usuarios');

ALTER TABLE `employees`
  ADD PRIMARY KEY (`IdEmploy`),
  ADD KEY `RolAsignado` (`IdRoles`);

ALTER TABLE `roles`
  ADD PRIMARY KEY (`IdRoles`);

ALTER TABLE `employees`
  MODIFY `IdEmploy` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=109;

ALTER TABLE `roles`
  MODIFY `IdRoles` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

ALTER TABLE `employees`
  ADD CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`IdRoles`) REFERENCES `roles` (`IdRoles`);
COMMIT;