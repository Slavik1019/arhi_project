import java.util.ArrayList;
import java.util.List;

public class GeometryFigure {
    private List<IShape> toolbox;

    public GeometryFigure() {
        toolbox = new ArrayList<>();
    }
    // Метод для добавления новой фигуры
    public void add(IShape figure) {
        toolbox.add(figure);
    }
    // Метод для удаления фигуры по индексу
    public void remove(int index) {
        if (index >= 0 && index < toolbox.size()) {
            toolbox.remove(index);
        } else {
            System.out.println("Неверный индекс для удаления фигуры.");
        }
    }
    // Метод поиска необходимой фигуры
    public IShape find(int index) {
        if (index >= 0 && index < toolbox.size()) {
            return toolbox.get(index);
        } else {
            System.out.println("Неверный индекс для поиска фигуры.");
            return null;
        }
    }
    // Метод отображения подробной информации о фигурк
    public void getInfo(int index) {
        IShape figure = find(index);
        if (figure != null) {
            if (figure instanceof Circle) {
                System.out.println("Тип: Круг");
                System.out.println("Площадь круга: " + figure.getArea());
                System.out.println("Периметр круга: " + figure.getPerimeter());
            } else if (figure instanceof Square) {
                System.out.println("Тип: Квадрат");
                System.out.println("Площадь квадрата: " + figure.getArea());
                System.out.println("Периметр квадрата: " + figure.getPerimeter());
            } else if (figure instanceof Triangle) {
                System.out.println("Тип: Треугольник");
                System.out.println("Площадь треугольника: " + figure.getArea());
                System.out.println("Периметр треугольника: " + figure.getPerimeter());
            } else {
                System.out.println("Неизвестный тип фигуры");
            }
        }
    }

}