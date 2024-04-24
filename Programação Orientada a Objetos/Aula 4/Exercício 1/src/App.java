public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        Livro harry = new LivroDigital("Harry Potter", "Magia", 1, new Autor("null", "null", "Britanica"), 1, 1.2);
        harry.info();
    }
}
