public class Ingresso {
    private String nomeEvento;
    private double valor;
    //COnstrutor
    /**
     * @param nomeEvento
     * @param valor
     */
    public Ingresso(String nomeEvento, double valor) {
        this.nomeEvento = nomeEvento;
        this.valor = valor;
    }

    //Métodos
    public void imprimir(){
        System.out.println("Nome do Evento: " + nomeEvento);
        System.out.println("Valor: " + valor);
    }


    

}
