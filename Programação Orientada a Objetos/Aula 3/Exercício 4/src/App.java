public class App {
    public static void main(String[] args) throws Exception {
        Cofrinho cofre = new Cofrinho();
        Moeda cinquenta = new Moeda(50, "centavos");
        cofre.adicionar(cinquenta);
        
    }
}
