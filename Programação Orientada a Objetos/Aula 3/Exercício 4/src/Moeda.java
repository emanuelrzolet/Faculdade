public class Moeda {

    private double valor;
    private String nome;

    //Metodos
    public Moeda(double valor, String nome){
        this.nome = nome;
        this.valor = valor;
    }

    /**
     * @return the valor
     */
    public double getValor() {
        return valor;
    }
    /**
     * @return the nome
     */
    public String getNome() {
        return nome;
    }

}
