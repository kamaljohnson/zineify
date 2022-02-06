<template>
	<div class="flex h-screen">
		<div class="m-auto">
			<Feed :zineId="zineId"/>
			<div class="m-auto">
				<div>
					<Button class="float-left" icon="chevron-left" @click="onPreviousClick()"/>
					<Button class="float-right" icon="chevron-right" @click="onNextClick()"/>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Feed from './Feed.vue'

export default {
	name: 'Feeds',
	data() {
		return {
			zineId: 0
		}
	},
	components: {
		Feed
	},
	methods: {
		onNextClick() {
			this.zineId++;
		},
		onPreviousClick() {
			this.zineId--;
		}
	}
}
</script>

<style>

</style>