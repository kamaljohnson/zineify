<template>
	<div class="flex h-screen">
		<div class="m-auto">
			<div style="width:400px; height: 650px">
				<Presence>
					<Motion
						v-show="showZine"
						:initial="{ x: [100, -50, 0] }"
						:exit="{ x: [-500] }"
					>
						<Motion>
							<Card title="Article Title" style="width: 400px;" :style="'height: ' + zineCardWidth + 'px;'" @click="onZineCardClick()">
								<span class="overflow-auto">
									Test Article means, in accordance with 21 C.F.R. § 50.3(j), any drug (including a biological product), medical device, food additive, color additive, electronic product, or any other article subject to regulation under the Federal Food, Drug, and Cosmetic Act that is intended for administration to humans or animals, including a drug or biologic as identified in the Research Plan and Appendix B, that is used within the scope of the Research Plan. The Test Article may also be referred to as Investigational Agent, Study Material, or Study Product.
								</span>
							</Card>
						</Motion>
						<Motion>
							<Card class="my-5 pt-2" style="width: 400px;" :style="'height: ' + chatCardWidth + 'px;'" @click="onChatCardClick()">
								<div class="overflow-auto" :style="'height: ' + (chatCardWidth - 75) + 'px;'">
									<ListItem title="Kamal" subtitle="This is a really cool article, can you please share the link for getting more info on this please"></ListItem>
									<ListItem title="Aditya" subtitle="I don't know the original article, I got this from my friend 😅, But I dont think it would be really hard to get this, a simple google search will fetch you enough info"></ListItem>
									<ListItem title="Hey" subtitle="This is a message"></ListItem>
									<ListItem title="Hey" subtitle="This is a message"></ListItem>
									<ListItem title="Hey" subtitle="This is a message"></ListItem>
									<ListItem title="Hey" subtitle="This is a message"></ListItem>
								</div>
								<Input type="text" value="" placeholder="Type your message..." />
							</Card>
						</Motion>
					</Motion>
				</Presence>
			</div>
			<div>
				<Button class="float-left" icon="chevron-left" @click="onPreviousClick()"/>
				<Button class="float-right" icon="chevron-right" @click="onNextClick()"/>
			</div>
		</div>
	</div>
</template>

<script>
import { Card, ListItem, Input } from 'frappe-ui'
import { Motion, Presence } from "motion/vue"

export default {
	name: 'Feeds',
	data() {
		return {
			chatCardWidth: 200,
			zineCardWidth: 400,
			showZine: true,
		}
	},
	components: {
		Card,
		ListItem,
		Input,
		Motion,
		Presence,
	},
	methods: {
		onChatCardClick() {
			this.chatCardWidth = 350;
			this.zineCardWidth = 250;
		},
		onZineCardClick() {
			this.chatCardWidth = 200;
			this.zineCardWidth = 400;
		},
		onNextClick() {
			this.showZine = false;
		},
		onPreviousClick() {
			this.showZine = true;
		}
	}
}
</script>

<style>

</style>