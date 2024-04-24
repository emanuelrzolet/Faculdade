public class Curso {
    String nome;
    float mensalidade;

    Curso(String nome, float mensalidade){
        this.nome = nome;
        this.mensalidade = mensalidade;
    }

    //Métodos
    void descrever(){
        System.out.println("Nome: " + nome);
        System.out.println("Mensalidade: " + mensalidade);
    }

}
