package ModelElements;

public class Scene {
    private PoligonalModel models;
    private Flash flashes;
    private Camera cameras;

    public Scene(PoligonalModel models, Flash flashes, Camera cameras) {
        this.models = models;
        this.flashes = flashes;
        this.cameras = cameras;
    }

}