       IDENTIFICATION DIVISION.
       PROGRAM-ID. backUrubu.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
           01 cmd-line        PIC X(80) VALUE SPACES.
           01 arg1-str        PIC X(20) VALUE SPACES.
           01 arg2-str        PIC X(20) VALUE SPACES.
           01 user-value      PIC 9(5)V99.
           01 days            PIC 9(3)V99 VALUE 30.
           01 result          PIC 9(9)V99.
           01 invalid-result  PIC X(9) VALUE 'true'.
           01 calc            PIC 9(9)V99.
           01 cpf-digited     PIC X(11) VALUE SPACES.
       procedure division.
           ACCEPT cmd-line FROM COMMAND-LINE

           UNSTRING cmd-line
               DELIMITED BY SPACE
               INTO arg1-str
                    arg2-str
                    cpf-digited
           END-UNSTRING

           
           DISPLAY invalid-result
           STOP RUN.

           MOVE FUNCTION NUMVAL(arg1-str) TO user-value

           IF arg2-str NOT = SPACES
               MOVE FUNCTION NUMVAL(arg2-str) TO days
           END-IF

           COMPUTE calc = (user-value / 100 * 33.33) * days
           MOVE calc TO result
           
           DISPLAY result
           STOP RUN.
