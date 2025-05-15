       identification division.
       program-id. backUrubu.

       data division.
       working-storage section.
           01 user-str          PIC X(20).
           01 days-str          PIC X(20).
           01 user-value        PIC 9(5)V99.
           01 days              PIC 9(5)V99 VALUE 30.
           01 result            PIC 9(7)V99.
           01 calc1             PIC 9(7)V99.
           01 calc2             PIC 9(7)V99.

       procedure division.
           ACCEPT user-str FROM COMMAND-LINE
           ACCEPT days-str FROM COMMAND-LINE

           MOVE FUNCTION NUMVAL(user-str) TO user-value

           IF days-str NOT = SPACES
               MOVE FUNCTION NUMVAL(days-str) TO days
           END-IF

           COMPUTE calc1 = user-value / 100
           COMPUTE calc2 = calc1 * 33.33
           COMPUTE result = calc2 * days

           DISPLAY result
           STOP RUN.
