INSERT_PESSOA = """
        INSERT INTO PESSOA(EMAIL, NOME, CPF, DATA_NASCIMENTO, TELEFONE, 
                            LOGRADOURO, BAIRRO, CIDADE, CEP, UF, COMPLEMENTO)
        VALUES ( :email, :nome, :cpf, TO_DATE( :data_nasc, 'DD/MM/YYYY'), :telefone, 
                    :logradouro, :bairro, :cidade, :cep, :uf, :complemento )
"""

INSERT_ALUNO = """
        INSERT INTO ALUNO(ID, ESCOLARIDADE, EXPERIENCIA_PROFISSIONAL)
                VALUES (
                        (SELECT P.ID FROM PESSOA P WHERE P.CPF= :cpf ),
                        :escolaridade , :experiencia )
"""

INSERT_FUNCAO = """
        INSERT INTO FUNCAO(PESSOA, FUNCAO)
                VALUES ((SELECT P.ID FROM PESSOA P WHERE P.CPF= :cpf ), 'ALUNO')
"""

INSERT_ALUNO_GRUPO = """
        INSERT INTO ALUNO_GRUPO(ALUNO, GRUPO)
                VALUES((SELECT A.ID FROM ALUNO A JOIN PESSOA P ON A.ID = P.ID WHERE P.CPF= :cpf), :grupo)
"""

SELECT_ALUNO_BY_EMAIL = """
SELECT P.EMAIL, P.NOME, P.CPF, P.DATA_NASCIMENTO, P.TELEFONE, P.LOGRADOURO,
        P.BAIRRO, P.CIDADE, P.CEP, P.UF, P.COMPLEMENTO FROM PESSOA P
    JOIN ALUNO A ON A.ID = P.ID
    WHERE P.EMAIL = :email
"""

SELECT_ALUNO_BY_EMAIL = """
SELECT P.EMAIL, P.NOME, P.CPF, P.DATA_NASCIMENTO, P.TELEFONE, P.LOGRADOURO,
        P.BAIRRO, P.CIDADE, P.CEP, P.UF, P.COMPLEMENTO FROM PESSOA P
    JOIN ALUNO A ON A.ID = P.ID
    WHERE P.EMAIL = :email
"""

SELECT_GRUPO_BY_EMAIL = """
SELECT AG.GRUPO FROM PESSOA P JOIN ALUNO A 
       ON A.ID = P.ID JOIN ALUNO_GRUPO AG
       ON AG.ALUNO = A.ID
       WHERE P.EMAIL = :email
"""

LIST_ALUNOS_BY_GRUPO = """
SELECT P.NOME, P.CPF FROM PESSOA P JOIN ALUNO A
       ON A.ID = P.ID JOIN ALUNO_GRUPO AG
       ON AG.ALUNO = A.ID JOIN GRUPO G
       ON G.NOME = AG.GRUPO
       WHERE G.NOME = :grupo
"""
