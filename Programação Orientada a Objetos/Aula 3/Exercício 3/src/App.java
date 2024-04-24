public class App {
    public static void main(String[] args) throws Exception {
        Curso curso1 = new Curso("Ads", 500);
        Aluno aluno1 = new Aluno("Emanuel", 1, 0.1, curso1);
        curso1.descrever();
        aluno1.descrever();
        System.out.println(aluno1.pagamento());
    }
}
