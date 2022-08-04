Projeto de site para adoção de animais

#Linguagem:
1. Django
2. Html
3. CSS

#Pendências:
1. Testes
2. Aperfeiçoamento de estilo e layout
3. Criação de método search e seu layout.


#O que foi feito até agora?
Para explicar, partiremos da premissa que foram feitos dois apps com django, um com nome users e outro com nome dogncat.
O primeiro possui cinco urls: 1. Cadastro, 2. Login, 3. Dashboard, 4. Logout, 5. Newpet.
O segundo possui dois urls: 1. Home, 2. Animal.

Os métodos de view não são de alta complexidade, então não escreverei sobre cada um especificamente.

Os models estão apenas no app dogncat. A class é Animal e possui os fields: 1. name, 2. description, 3.castracao, 4. porte, 5. cidade, 6. created_at, 7. update_at, 8. is_staff, 9. tyoe_of_animal, 10. cover e 11. author.

