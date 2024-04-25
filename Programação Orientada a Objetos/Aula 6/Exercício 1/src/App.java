public class App {
    public static void main(String[] args) throws Exception {
        Conta conta1 = new Conta();
        Conta conta2 = new Conta();
        conta1.setSaldo(800);
        conta1.depositar(5);
        conta1.transferir(50, conta2);
        
    }
}
