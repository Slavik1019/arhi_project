package Rewards.Ruby;

import Abstractions.IGameItem;
import Abstractions.ItemGenerator;

public class RubyGenerator extends ItemGenerator {
    @Override
    public IGameItem createItem() {
        return new RubyRewards();
    }
}