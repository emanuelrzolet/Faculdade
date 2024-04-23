public class App {
    public static void main(String[] args) throws Exception {
        Avaliacao avaliacao1 = new Avaliacao(10, 5, 8);
        Aluno carlos = new Aluno("Carlos", "Agronomia", avaliacao1);
        carlos.verAluno("Carlos");
    }
}
