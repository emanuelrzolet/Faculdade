public class LivroDigital extends Livro{
    private int download;
    private double tamanho;
    
    public LivroDigital(String titulo, String genero, int edicao, Autor autor, int download, double tamanho) {
        super(titulo, genero, edicao, autor);
        this.download = download;
        this.tamanho = tamanho;
    }

    /**
     * @return the download
     */
    public int getDownload() {
        return download;
    }

    /**
     * @param download the download to set
     */
    public void setDownload(int download) {
        this.download = download;
    }

    /**
     * @return the tamanho
     */
    public double getTamanho() {
        return tamanho;
    }

    /**
     * @param tamanho the tamanho to set
     */
    public void setTamanho(double tamanho) {
        this.tamanho = tamanho;
    }

}
