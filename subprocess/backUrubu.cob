       identification division.
       program-id. backUrubu.

       data division.
       working-storage section.
           01 user-value        PIC 9(5)V99.
           01 result            PIC 9(7)V99.
           01 calc1             PIC 9(7)V99.
           01 calc2             PIC 9(7)V99.
           01 argument          PIC X(20).

       procedure division.
           accept argument from command-line
           move function numval(argument) to user-value

           compute calc1 = user-value / 100
           compute calc2 = calc1 * 33.33
           compute result = calc2 * 30

           display result
           stop run.
           