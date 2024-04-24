public class Nota {
    private double nota1, nota2;
    private int faltas;

    Nota(double nota1, double nota2){}
    public void addFaltas(){
        faltas ++;
    }
    
    public void setNota1(double valor){
        this.nota1 = valor;
    }
    public void setNota2(double valor){
        this.nota2 = valor;
    }
    public double getNota1(){return nota1;}
    public double getNota2(){return nota2;}
    
    void resultado(){
        if (faltas > 7) {
            System.out.println("Aluno reprovado por faltas!");
            
        }
        else{
        double media = (nota1 + nota2) / 2;
        if (media > 6) {
            System.out.println("Aluno aprovado");
            
        }
        else if (media >= 5 && media <=6){
            System.out.println("Aluno em exame.");}
        else if (media < 5){
            System.out.println("Aluno Reprovado");

        }}
    }



}
