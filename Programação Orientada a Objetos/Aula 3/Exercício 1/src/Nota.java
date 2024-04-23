public class Nota {
    private double nota1, nota2;
    
    public void setNota1(double valor){
        this.nota1 = valor;
    }
    public void setNota2(double valor){
        this.nota2 = valor;
    }
    public double getNota1(){return nota1;}
    public double getNota2(){return nota2;}
    
    void resultado(){
        double media = (nota1 + nota2) / 2;
        if (media > 6) {
            System.out.println("Aluno aprovado");
            
        }
        else if (media >= 5 && media <=6){
            System.out.println("Aluno em exame.");}
        else if (media < 5){
            System.out.println("Aluno Reprovado");

        }
    }



}
