public class Car implements ICar, FuelStation {
    protected String mark, model, color, exter, fluel_type, control;
    protected int num_wheels;
    protected double vol_eng;

    private boolean light_on;

    @Override
    public void isLight_on(boolean is_light) {
        light_on = is_light;
    }

    public Car(String mark, String model, String color, String exter, String fluel_type, String control, int num_wheels, double vol_eng) {
        this.mark = mark;
        this.model = model;
        this.color = color;
        this.exter = exter;
        this.fluel_type = fluel_type;
        this.control = control;
        this.num_wheels = num_wheels;
        this.vol_eng = vol_eng;
    }

    protected String movement() {
        return "";
    }

    protected String service() {
        return "";
    }

    public void changeControl(String control_mode) {
    }

    @Override
    public boolean isSweepingStreet(boolean isSweeping) {
        return false;
    }

    @Override
    public void refuel() {
        // Реализация метода заправки
    }

    @Override
    public void cleanWindshield() {
        // Реализация метода протирки лобового стекла
    }

    @Override
    public void cleanHeadlights() {
        // Реализация метода протирки фар
    }

    @Override
    public void cleanMirrors() {
        // Реализация метода протирки зеркал
    }
}