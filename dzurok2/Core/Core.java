package Core;

import Abstractions.ItemGenerator;
import Rewards.Gold.GoldGenerator;
import Rewards.Silver.SilverGenerator;
import Rewards.Ruby.RubyGenerator;
import Rewards.Diamond.DiamondGenerator;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Core {
    // Логика игры
    public void run() {
        // Создаем список генераторов для продуктов
        List<ItemGenerator> generatorList = new ArrayList<>();
        generatorList.add(new GoldGenerator());
        generatorList.add(new SilverGenerator());
        generatorList.add(new RubyGenerator());
        generatorList.add(new DiamondGenerator());

        Random random = new Random(); // Создаем объект Random для генерации случайных чисел

        // Цикл для выбора и вывода 4 продуктов
        for (int i = 0; i < 4; i++) { 
            int randomIndex = random.nextInt(generatorList.size());
            ItemGenerator myGenerator = generatorList.get(randomIndex);
            System.out.println(myGenerator.openReward());
            generatorList.remove(randomIndex); // Удаляем использованный генератор, чтобы избежать повторений
        }
    }
}