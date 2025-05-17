       IDENTIFICATION DIVISION.
       PROGRAM-ID. cpf_validator.
        
       DATA DIVISION.
           LOCAL-STORAGE SECTION.
            01 LS-CPFTEMP.
              05 D1T PIC 9.
              05 D2T PIC 9.
              05 D3T PIC 9.
              05 D4T PIC 9.
              05 D5T PIC 9.
              05 D6T PIC 9.
              05 D7T PIC 9.
              05 D8T PIC 9.
              05 D9T PIC 9.
              05 D10T PIC 9.
              05 D11T PIC 9.
              
            77 LS-CALCULAR PIC 9999.
            77 LS-C PIC 99 VALUE 00.
            77 LS-R PIC 99 VALUE 00.
        
       LINKAGE SECTION.
            77 L-CPF PIC 9(11).
            77 L-STATUS PIC 9.
        
       PROCEDURE DIVISION USING L-CPF,L-STATUS.
           MOVE L-CPF TO LS-CPFTEMP.
 
           COMPUTE LS-CALCULAR = (D1T * 10) +  (D2T * 9) + (D3T * 8) + 
            (D4T * 7) + (D5T * 6) + (D6T * 5) + (D7T * 4) + (D8T * 3) + 
            (D9T * 2).
		    
           DIVIDE LS-CALCULAR BY 11 GIVING LS-C REMAINDER LS-R.

           IF LS-R < 2 THEN
              MOVE 0 TO D10T
           ELSE
              COMPUTE D10T = 11 - LS-R
           END-IF.

           COMPUTE LS-CALCULAR = (D1T * 11) +  (D2T * 10) + (D3T * 9)+ 
            (D4T * 8) + (D5T * 7) + (D6T * 6) + (D7T * 5) + (D8T * 4) + 
            (D9T * 3) + (D10T * 2).

           DIVIDE LS-CALCULAR BY 11 GIVING LS-C REMAINDER LS-R.
			
           IF LS-R < 2 THEN
              MOVE 0 TO D11T
           ELSE
              COMPUTE D11T = 11 - LS-R
           END-IF.

           IF L-CPF = LS-CPFTEMP THEN
               MOVE 1 TO L-STATUS
           ELSE
               MOVE 0 TO L-STATUS
           END-IF.
            
           EXIT PROGRAM.