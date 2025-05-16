       IDENTIFICATION DIVISION.
       PROGRAM-ID. teste.

       DATA DIVISION.
       WORKING-STORAGE SECTION.           
           01 cpf-digited     PIC X(11) value "12345678910".
           01 result          PIC 9(9)V99.
           01 invalid-msg     PIC X(9) value "Invalid".
       procedure division.
           if cpf-digited = "12345678910"
               MOVE 2 to result
               display result
           else
               display invalid-msg
           END-IF.
           STOP RUN.
