public class App {
    public static void main(String[] args) throws Exception {
        Conta conta1 = new Conta(1, "Emanuel", 1000);
        conta1.info();
        conta1.deposita(100);
        conta1.sacar(100);
        conta1.info();
        conta1.sacar(10000);
        conta1.transferir(conta1, new Conta(2, "Paola", 5000), 800);
    }
}
