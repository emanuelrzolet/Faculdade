import java.util.ArrayList;

public class Cofrinho {

    private ArrayList<Moeda> moedas = new ArrayList();
    
    public Cofrinho(){

    }

    void adicionar(Moeda moeda){
        moedas.add(moeda);

    };
    double calcularTotal(){
        double total = 0;
        for (Moeda moeda : moedas) {
            total += moeda.getValor();
            
        }
        return total;
    };

}
