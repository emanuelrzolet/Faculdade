public class Aluno {

    
    String nome, curso;
    Avaliacao avaliacao;
    
    Aluno(String nome, String curso, Avaliacao avaliacao){
        this.nome = nome;
        this.curso = curso;
        this.avaliacao = avaliacao;
    }

    void verAluno(String nome){
        if (this.nome == nome) {
            System.out.println("Verificando informações do aluno...");
            System.out.println("Nome: " + this.nome);
            System.out.println("Curso: " + curso);
            System.out.println("Avaliação: " + avaliacao);
            
        }
        else{
            System.out.println("Aluno não encontrado");
        }

    }


}
