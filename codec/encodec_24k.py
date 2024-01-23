from base_codec.encodec import BaseCodec

class Codec(BaseCodec):
    def config(self):
        self.model = self.EncodecModel.encodec_model_24khz()
        self.model.set_target_bandwidth(6.0)
        self.sampling_rate = 24_000
