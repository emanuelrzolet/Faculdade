public class Aluno {
    String nome;
    int matricula;
    double desconto;
    Curso curso;

    /**
     * @param nome
     * @param matricula
     * @param desconto
     * @param curso
     */
    public Aluno(String nome, int matricula, double desconto, Curso curso) {
        this.nome = nome;
        this.matricula = matricula;
        this.desconto = desconto;
        this.curso = curso;
    }
    //Metodos
    void descrever(){};
    float pagamento(){
        return (float) (curso.mensalidade - desconto);
    }
    
}
