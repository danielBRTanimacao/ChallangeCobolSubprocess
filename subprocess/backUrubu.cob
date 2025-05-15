       identification division.
       program-id. backUrubu.

       data division.
       working-storage section.
           01 user-str          PIC x(20).
           01 days-str          PIC x(20).
           01 user-value        PIC 9(5)V99.
           01 days              PIC 9(5)V99 value 30.
           01 result            PIC 9(7)V99.
           01 calc1             PIC 9(7)V99.
           01 calc2             PIC 9(7)V99.

       procedure division.
           accept user-str from command-line
           move function numval(user-str) to user-value

           accept days-str from command-line
           if days-str not = space
               move function numval(days-str) to days
           end-if
               
           compute calc1 = user-value / 100
           compute calc2 = calc1 * 33.33
           compute result = calc2 * days

           display result
           stop run.
           