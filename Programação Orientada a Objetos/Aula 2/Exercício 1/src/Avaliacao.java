public class Avaliacao {
    double nota1;
    double nota2;
    double nota3;

    double calcMedAritmética(){
        return (nota1 + nota2 + nota3) / 3;
    }

    double calcMedPonderada(){
        return ((2 * nota1) + (3 * nota2) + (4 * nota3)) / (2 + 3 + 4);
    }


}
