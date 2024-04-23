public class Avaliacao {

    double nota1, nota2, nota3;
    Avaliacao(double nota1, double nota2, double nota3){
        this.nota1 = nota1;
        this.nota2 = nota2;
        this.nota3 = nota3;
    }

    double calcMedAritmética(){
        return (nota1 + nota2 + nota3) / 3;
    }

    double calcMedPonderada(){
        return ((2 * nota1) + (3 * nota2) + (4 * nota3)) / (2 + 3 + 4);
    }


}
