public class Main1 {
    public static void main(String[] args) {
        GeometryFigure figureBox = new GeometryFigure();

        // Создаем объекты фигур
        Circle circle1 = new Circle(10);
        Square square1 = new Square(5);
        Triangle triangle1 = new Triangle(3, 4, 5);

        // Добавляем фигуры в контейнер
        figureBox.add(circle1);
        figureBox.add(square1);
        figureBox.add(triangle1);

        // Выводим информацию о фигурах
        System.out.println("Информация о фигурах:");
        figureBox.getInfo(0); // Информация о круге
        figureBox.getInfo(1); // Информация о квадрате
        figureBox.getInfo(2); // Информация о треугольнике

        
        // Поиск фигуры по индексу
        System.out.println("\nПоиск фигуры по индексу:");
        IShape foundFigure = figureBox.find(2); // Ищем фигуру по индексу 2 (треугольник)
        if (foundFigure != null) {
            System.out.println("Найдена фигура:");
            if (foundFigure instanceof Circle) {
                System.out.println("Тип: Круг");
            } else if (foundFigure instanceof Square) {
                System.out.println("Тип: Квадрат");
            } else if (foundFigure instanceof Triangle) {
                System.out.println("Тип: Треугольник");
            } else {
                System.out.println("Неизвестный тип фигуры");
            }
            System.out.println("Площадь: " + foundFigure.getArea());
            System.out.println("Периметр: " + foundFigure.getPerimeter());
        } else {
            System.out.println("Фигура не найдена.");
        }
        // Удаляем фигуру (например, круг)
            figureBox.remove(0);
            System.out.println("\nУдален круг.");
    }
}