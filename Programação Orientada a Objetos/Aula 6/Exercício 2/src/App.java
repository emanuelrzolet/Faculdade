public class App {

    public static int[] instanciaArray(int n) throws NegativeArraySizeException{
        return new int[n];
    }
    public static void main(String[] args) throws Exception {
        int tam = -10;
        if (tam < 0) {
            throw new Exception("Digite um valor valido.");
            
        }
        int arr[] = instanciaArray(tam);
        for (int i=0; i < tam; i++){
            System.out.println(arr[i]);
        }
    }
}
