public class AirCar extends Car {
    public AirCar(String mark, String model, String color, String exter, String fluel_type, String control, int num_wheels, double vol_eng) {
        super(mark, model, color, exter, fluel_type, control, num_wheels, vol_eng);
    }

    @Override
    protected String movement() {
        return "Flying"; // Реализация метода "полет"
    }

    protected String drive() {
        return "Driving"; // Реализация метода "движение"
    }
}